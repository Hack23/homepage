#!/usr/bin/env python3
"""
Script to create 10 GitHub issues using Personal Access Token.
Usage: GITHUB_TOKEN=your_token python3 create_issues_with_pat.py
"""

import json
import urllib.request
import urllib.error
import os
import sys
import time

def create_github_issue(issue_data, token, repo='Hack23/homepage'):
    """Create a GitHub issue using REST API"""
    url = f"https://api.github.com/repos/{repo}/issues"
    
    data = {
        "title": issue_data['title'],
        "body": issue_data['body'],
        "labels": issue_data['labels']
    }
    
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github+json',
        'Content-Type': 'application/json',
        'X-GitHub-Api-Version': '2022-11-28',
        'User-Agent': 'Copilot-Agent-Translation-Issues'
    }
    
    try:
        req = urllib.request.Request(
            url,
            data=json.dumps(data).encode('utf-8'),
            headers=headers,
            method='POST'
        )
        
        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode('utf-8'))
            return {
                'success': True,
                'number': result.get('number'),
                'url': result.get('html_url'),
                'title': result.get('title')
            }
    
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        try:
            error_data = json.loads(error_body)
            error_msg = error_data.get('message', error_body)
        except:
            error_msg = error_body
        
        return {
            'success': False,
            'error': f"HTTP {e.code}: {error_msg}",
            'code': e.code
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def main():
    print("=" * 80)
    print("GITHUB ISSUE CREATOR - Translation Completion")
    print("=" * 80)
    print()
    
    # Try to find GitHub token
    token = None
    token_sources = [
        'GITHUB_TOKEN',
        'GH_TOKEN',
        'COPILOT_MCP_GITHUB_PERSONAL_ACCESS_TOKEN',
        'PAT',
        'GITHUB_PAT'
    ]
    
    for source in token_sources:
        if os.getenv(source):
            token = os.getenv(source)
            print(f"✓ Found token from: {source}")
            break
    
    if not token:
        print("❌ ERROR: No GitHub token found")
        print()
        print(f"Checked environment variables: {', '.join(token_sources)}")
        print()
        print("Please provide a GitHub Personal Access Token:")
        print()
        print("  export GITHUB_TOKEN='your_token_here'")
        print("  python3 create_issues_with_pat.py")
        print()
        print("Or:")
        print()
        print("  GITHUB_TOKEN='your_token' python3 create_issues_with_pat.py")
        print()
        print("The token needs 'repo' scope to create issues.")
        print()
        sys.exit(1)
    
    print(f"  Token preview: {token[:8]}...{token[-4:]}")
    print()
    
    # Load manifest
    try:
        with open('issues_manifest.json', 'r') as f:
            manifest = json.load(f)
    except FileNotFoundError:
        print("❌ ERROR: issues_manifest.json not found")
        print("   Please run this script from the repository root directory")
        sys.exit(1)
    
    print(f"Loaded {len(manifest['issues'])} issues from manifest")
    print()
    print("Creating issues...")
    print()
    
    # Create issues
    created_issues = []
    failed_issues = []
    
    for issue_data in manifest['issues']:
        issue_num = issue_data['number']
        title_preview = issue_data['title'][:65] + "..." if len(issue_data['title']) > 65 else issue_data['title']
        
        print(f"Issue {issue_num}/10: {title_preview}")
        
        result = create_github_issue(issue_data, token)
        
        if result['success']:
            print(f"  ✅ Created #{result['number']}: {result['url']}")
            created_issues.append({
                'number': issue_num,
                'github_number': result['number'],
                'title': issue_data['title'],
                'url': result['url']
            })
        else:
            print(f"  ❌ Failed: {result['error'][:100]}")
            failed_issues.append({
                'number': issue_num,
                'title': issue_data['title'],
                'error': result['error']
            })
        
        print()
        
        # Rate limiting - small delay between requests
        time.sleep(1.5)
    
    # Summary
    print("=" * 80)
    print(f"ISSUE CREATION SUMMARY")
    print("=" * 80)
    print()
    print(f"✅ Successfully Created: {len(created_issues)}/10 issues")
    print(f"❌ Failed: {len(failed_issues)}/10 issues")
    print()
    
    if created_issues:
        print("📋 CREATED ISSUES:")
        print("-" * 80)
        for issue in created_issues:
            print(f"  #{issue['github_number']}: {issue['title']}")
            print(f"     {issue['url']}")
            print()
        print()
    
    if failed_issues:
        print("❌ FAILED ISSUES:")
        print("-" * 80)
        for issue in failed_issues:
            print(f"  {issue['number']}. {issue['title'][:70]}")
            print(f"     Error: {issue['error'][:150]}")
            print()
        print()
        print("⚠️  For failed issues, see CREATE_ISSUES_INSTRUCTIONS.md for manual creation")
        print()
    
    # Save results
    results = {
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'repository': 'Hack23/homepage',
        'created': created_issues,
        'failed': failed_issues,
        'total': len(manifest['issues']),
        'success_count': len(created_issues),
        'failure_count': len(failed_issues)
    }
    
    with open('issue_creation_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"💾 Results saved to: issue_creation_results.json")
    print()
    
    if created_issues:
        print("🎉 SUCCESS! Issues created successfully!")
        print()
        print("Next steps:")
        print("  1. Review issues at: https://github.com/Hack23/homepage/issues")
        print("  2. Assign to: copilot-swe-agent[bot]")
        print("  3. Monitor translation progress")
        print()
    
    print("=" * 80)
    
    return 0 if not failed_issues else 1

if __name__ == '__main__':
    sys.exit(main())

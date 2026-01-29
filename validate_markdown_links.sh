#!/bin/bash
# Markdown Link Validator for Hack23AB directory
# Validates that all relative links in markdown files resolve correctly

echo "🔍 Validating Markdown Links in Hack23AB Directory"
echo "================================================="
echo ""

# Ensure we're running in a subshell or save the original directory
ORIGINAL_DIR="$(pwd)"
cd "$(dirname "$0")"
ROOT_DIR="$(pwd)"
FAIL_COUNT=0

# Function to test if a file exists relative to a source directory
test_link() {
    local source_file="$1"
    local link_path="$2"
    local source_dir="$(dirname "$source_file")"
    
    # Use subshell to avoid changing caller's directory
    (
        cd "$ROOT_DIR" || return 1
        cd "$source_dir" 2>/dev/null || return 1
        
        # Remove anchor from link
        local file_path="${link_path%%#*}"
        
        if [ -f "$file_path" ]; then
            echo "  ✅ $link_path"
            return 0
        else
            echo "  ❌ $link_path (NOT FOUND)"
            return 1
        fi
    )
}

# Check that source files exist
if [ ! -f "Hack23AB/Marketing/Linkedin/LinkedIn_Analytics_Report_2025.md" ]; then
    echo "❌ Source file not found: Hack23AB/Marketing/Linkedin/LinkedIn_Analytics_Report_2025.md"
    exit 1
fi

if [ ! -f "Hack23AB/Marketing/SearchEngines/Google/Google_Search_Console_Report_2025.md" ]; then
    echo "❌ Source file not found: Hack23AB/Marketing/SearchEngines/Google/Google_Search_Console_Report_2025.md"
    exit 1
fi

# Test LinkedIn Analytics Report links
echo "📄 Testing: Hack23AB/Marketing/Linkedin/LinkedIn_Analytics_Report_2025.md"
echo ""

test_link "Hack23AB/Marketing/Linkedin/LinkedIn_Analytics_Report_2025.md" "../../../CLASSIFICATION.md#confidentiality-levels" || ((FAIL_COUNT++))
test_link "Hack23AB/Marketing/Linkedin/LinkedIn_Analytics_Report_2025.md" "../../../Business_Strategy.md" || ((FAIL_COUNT++))
test_link "Hack23AB/Marketing/Linkedin/LinkedIn_Analytics_Report_2025.md" "../../../Marketing_Strategy.md" || ((FAIL_COUNT++))
test_link "Hack23AB/Marketing/Linkedin/LinkedIn_Analytics_Report_2025.md" "../../../Marketing_Plan.md" || ((FAIL_COUNT++))
test_link "Hack23AB/Marketing/Linkedin/LinkedIn_Analytics_Report_2025.md" "../../../AnnualReport2025/Annual_Report_2025.md" || ((FAIL_COUNT++))

echo ""
echo "📄 Testing: Hack23AB/Marketing/SearchEngines/Google/Google_Search_Console_Report_2025.md"
echo ""

test_link "Hack23AB/Marketing/SearchEngines/Google/Google_Search_Console_Report_2025.md" "../../../../CLASSIFICATION.md#confidentiality-levels" || ((FAIL_COUNT++))
test_link "Hack23AB/Marketing/SearchEngines/Google/Google_Search_Console_Report_2025.md" "../../../../Business_Strategy.md" || ((FAIL_COUNT++))
test_link "Hack23AB/Marketing/SearchEngines/Google/Google_Search_Console_Report_2025.md" "../../../../Marketing_Strategy.md" || ((FAIL_COUNT++))
test_link "Hack23AB/Marketing/SearchEngines/Google/Google_Search_Console_Report_2025.md" "../../../../Marketing_Plan.md" || ((FAIL_COUNT++))
test_link "Hack23AB/Marketing/SearchEngines/Google/Google_Search_Console_Report_2025.md" "../../../../AnnualReport2025/Annual_Report_2025.md" || ((FAIL_COUNT++))
test_link "Hack23AB/Marketing/SearchEngines/Google/Google_Search_Console_Report_2025.md" "../../Linkedin/LinkedIn_Analytics_Report_2025.md" || ((FAIL_COUNT++))

echo ""
echo "================================================="

# Restore original directory
cd "$ORIGINAL_DIR"

if [ $FAIL_COUNT -eq 0 ]; then
    echo "✅ All markdown links validated successfully!"
    exit 0
else
    echo "❌ Found $FAIL_COUNT broken link(s)"
    exit 1
fi

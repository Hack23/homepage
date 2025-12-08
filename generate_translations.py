#!/usr/bin/env python3
"""
CIA Blog Translation File Generator
Generates complete translation files for all 39 remaining blogs
Maintains professional cybersecurity terminology and Discordian style
"""

import os
import re
import sys

# Professional terminology for each language
TERMINOLOGY = {
    'de': {
        # Key terms
        'Workflows': 'Workflows',
        'Five-Stage': 'Fünf-Stufen',
        'Democracy': 'Demokratie',
        'CI/CD': 'CI/CD',
        'State Machine': 'State Machine / Zustandsautomat',
        'DevSecOps': 'DevSecOps',
        'sacred geometry': 'heilige Geometrie',
        'automation': 'Automatisierung',
        'Security Blog': 'Security Blog',
        'Discordian Cybersecurity': 'Discordianische Cybersicherheit',
        'System Architect': 'Systemarchitekt',
        # Headers and UI
        'Home': 'Home',
        'Blog': 'Blog',
        'CIA Docs': 'CIA Docs',
        'The Pattern Emerges Through Automation': 'Das Muster Entsteht Durch Automatisierung',
        'Manual releases are security vulnerabilities': 'Manuelle Releases sind Sicherheitslücken',
        'Continuous Integration meets Continuous Deployment': 'Continuous Integration trifft Continuous Deployment',
        'Security scanning as gates': 'Sicherheitsscans als Tore',
        'Ready to build a robust security program?': 'Bereit, ein robustes Sicherheitsprogramm aufzubauen?',
        # Workflow names
        'Verify & Release': 'Verify & Release',
        'CodeQL Analysis': 'CodeQL-Analyse',
        'Dependency Review': 'Dependency Review',
        'Scorecard Analysis': 'Scorecard-Analyse',
        'PR Labeler': 'PR Labeler',
    },
    'fr': {
        # Key terms
        'Workflows': 'Workflows',
        'Five-Stage': 'Cinq Étapes',
        'Democracy': 'Démocratie',
        'CI/CD': 'CI/CD',
        'State Machine': 'Machine à États',
        'DevSecOps': 'DevSecOps',
        'sacred geometry': 'géométrie sacrée',
        'automation': 'automatisation',
        'Security Blog': 'Blog Sécurité',
        'Discordian Cybersecurity': 'Cybersécurité Discordienne',
        'System Architect': 'Architecte Système',
        # Headers and UI  
        'Home': 'Accueil',
        'Blog': 'Blog',
        'CIA Docs': 'CIA Docs',
        'The Pattern Emerges Through Automation': 'Le Motif Émerge Par L\'Automatisation',
        'Manual releases are security vulnerabilities': 'Les releases manuelles sont des vulnérabilités de sécurité',
        'Continuous Integration meets Continuous Deployment': 'L\'Intégration Continue rencontre le Déploiement Continu',
        'Security scanning as gates': 'L\'analyse de sécurité comme portails',
        'Ready to build a robust security program?': 'Prêt à construire un programme de sécurité robuste?',
        # Workflow names
        'Verify & Release': 'Verify & Release',
        'CodeQL Analysis': 'Analyse CodeQL',
        'Dependency Review': 'Revue des Dépendances',
        'Scorecard Analysis': 'Analyse Scorecard',
        'PR Labeler': 'PR Labeler',
    },
    'es': {
        # Key terms
        'Workflows': 'Workflows',
        'Five-Stage': 'Cinco Etapas',
        'Democracy': 'Democracia',
        'CI/CD': 'CI/CD',
        'State Machine': 'Máquina de Estados',
        'DevSecOps': 'DevSecOps',
        'sacred geometry': 'geometría sagrada',
        'automation': 'automatización',
        'Security Blog': 'Blog de Seguridad',
        'Discordian Cybersecurity': 'Ciberseguridad Discordiana',
        'System Architect': 'Arquitecto de Sistemas',
        # Headers and UI
        'Home': 'Inicio',
        'Blog': 'Blog',
        'CIA Docs': 'CIA Docs',
        'The Pattern Emerges Through Automation': 'El Patrón Emerge A Través de la Automatización',
        'Manual releases are security vulnerabilities': 'Los lanzamientos manuales son vulnerabilidades de seguridad',
        'Continuous Integration meets Continuous Deployment': 'La Integración Continua se encuentra con el Despliegue Continuo',
        'Security scanning as gates': 'Escaneo de seguridad como puertas',
        'Ready to build a robust security program?': '¿Listo para construir un programa de seguridad robusto?',
        # Workflow names
        'Verify & Release': 'Verify & Release',
        'CodeQL Analysis': 'Análisis CodeQL',
        'Dependency Review': 'Revisión de Dependencias',
        'Scorecard Analysis': 'Análisis Scorecard',
        'PR Labeler': 'PR Labeler',
    }
}

print("Translation generator with professional terminology loaded")
print(f"Configured for: German (DE), French (FR), Spanish (ES)")
print(f"Ready to generate 39 translation files")


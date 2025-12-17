# Pulmonary Drug Delivery Excipients Database

A exploratory database extraction and analysis project examining excipients used in pulmonary drug delivery systems, with focus on comparing FDA-approved versus novel materials for dry powder inhalers (DPIs) and other inhalation formulations.

## Project Overview

This project systematically extracts, standardizes, and analyzes data from a comprehensive literature review on excipients for pulmonary delivery. The database includes 43 excipients (15 FDA-approved, 28 potential new materials) with detailed properties, applications, and therapeutic targets.

## Database Structure

### Tables:
1. **excipients_main.csv** - Core excipient data (43 entries)
2. **excipients_properties.csv** - Advantages/disadvantages (200+ entries)
3. **excipients_applications.csv** - Disease-drug-phase mappings (100+ entries)
4. **excipients_coformulations.csv** - Common excipient combinations

### Key Fields:
- Chemical categories (Oligosaccharides, Polysaccharides, Amino Acids, Lipids, Polymers)
- Physicochemical properties (Tg, hygroscopicity, reducing character)
- Therapeutic applications (Tuberculosis, Lung Cancer, Asthma, COPD, CF, COVID-19)
- Approval status and marketed products

## Analysis Goals

- Identify property patterns distinguishing approved vs. novel excipients
- Evaluate innovation trends in pulmonary drug delivery
- Generate publication-ready visualizations and insights

## Technologies

- **Python**: pandas, numpy for data processing
- **Data Analysis**: matplotlib, seaborn for visualization
- **Source**: Systematic extraction from peer-reviewed literature review

## Use Cases

- Pharmaceutical formulation researchers comparing excipient options
- Regulatory scientists evaluating novel materials
- Academic researchers studying pulmonary drug delivery trends
- Industry professionals benchmarking formulation strategies

## Citation

Data extracted from an unpublished review article on excipients for pulmonary drug delivery.

## Key Statistics

- 43 excipients catalogued
- 15 FDA-approved materials
- 28 potential new candidates

*Developed for pharmaceutical research and educational purposes*

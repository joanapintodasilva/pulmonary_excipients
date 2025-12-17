import pandas as pd
import numpy as np

# MAIN EXCIPIENTS TABLE
excipients_data = {
    'Excipient_ID': [],
    'Excipient_Name': [],
    'Chemical_Category': [],
    'Approval_Status': [],
    'Tg_C': [],
    'Hygroscopicity': [],
    'Reducing_Character': [],
    'Primary_Function': [],
    'Melting_Point_Info': [],
    'Molecular_Weight_Info': []
}

# SECTION 2: CONVENTIONAL/APPROVED EXCIPIENTS

excipients = [
    # Sugars
    {
        'Excipient_ID': 'EXC001',
        'Excipient_Name': 'Lactose',
        'Chemical_Category': 'Oligosaccharide',
        'Approval_Status': 'FDA_Approved',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'High',
        'Reducing_Character': 'Yes',
        'Primary_Function': 'Carrier',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    {
        'Excipient_ID': 'EXC002',
        'Excipient_Name': 'Mannitol',
        'Chemical_Category': 'Polyol',
        'Approval_Status': 'FDA_Approved',
        'Tg_C': 'Low',
        'Hygroscopicity': 'Low',
        'Reducing_Character': 'No',
        'Primary_Function': 'Stabilizer/Osmotic_Agent',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    {
        'Excipient_ID': 'EXC003',
        'Excipient_Name': 'Glucose',
        'Chemical_Category': 'Monosaccharide',
        'Approval_Status': 'FDA_Approved',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'Yes',
        'Primary_Function': 'Carrier',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    
    # Amino Acids
    {
        'Excipient_ID': 'EXC004',
        'Excipient_Name': 'Glycine',
        'Chemical_Category': 'Amino_Acid',
        'Approval_Status': 'FDA_Approved',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'Low',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Bulking_Agent',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': '0.25-1000_kDa'
    },
    
    # Phospholipids
    {
        'Excipient_ID': 'EXC005',
        'Excipient_Name': 'DSPC',
        'Chemical_Category': 'Phospholipid',
        'Approval_Status': 'FDA_Approved',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Shell_Former/Surfactant',
        'Melting_Point_Info': 'High',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    
    # Polymers
    {
        'Excipient_ID': 'EXC006',
        'Excipient_Name': 'Gelatin',
        'Chemical_Category': 'Protein_Polymer',
        'Approval_Status': 'FDA_Approved',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Stabilizer/Carrier',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    {
        'Excipient_ID': 'EXC007',
        'Excipient_Name': 'HPMC',
        'Chemical_Category': 'Cellulose_Derivative',
        'Approval_Status': 'FDA_Approved',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'No',
        'Primary_Function': 'Stabilizer/Mucoadhesive',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    {
        'Excipient_ID': 'EXC008',
        'Excipient_Name': 'Carrageenan',
        'Chemical_Category': 'Polysaccharide',
        'Approval_Status': 'FDA_Approved',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'No',
        'Primary_Function': 'Mucoadhesive/Gelling_Agent',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    {
        'Excipient_ID': 'EXC009',
        'Excipient_Name': 'Polysorbate_80',
        'Chemical_Category': 'Surfactant',
        'Approval_Status': 'FDA_Approved',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Surfactant/Stabilizer',
        'Melting_Point_Info': 'Low_semi-solid',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    
    # Electrolytes/Salts
    {
        'Excipient_ID': 'EXC010',
        'Excipient_Name': 'Calcium_Chloride',
        'Chemical_Category': 'Inorganic_Salt',
        'Approval_Status': 'FDA_Approved',
        'Tg_C': 'Not_Applicable',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Surface_Modifier/Stabilizer',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    {
        'Excipient_ID': 'EXC011',
        'Excipient_Name': 'Sodium_Chloride',
        'Chemical_Category': 'Inorganic_Salt',
        'Approval_Status': 'FDA_Approved',
        'Tg_C': 'Not_Applicable',
        'Hygroscopicity': 'High',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Osmolarity_Adjuster/Porogen',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    {
        'Excipient_ID': 'EXC012',
        'Excipient_Name': 'Sodium_Citrate',
        'Chemical_Category': 'Organic_Salt',
        'Approval_Status': 'FDA_Approved',
        'Tg_C': 'High',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Buffer/Glass_Former',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    
    # Lubricants/Glidants
    {
        'Excipient_ID': 'EXC013',
        'Excipient_Name': 'Magnesium_Stearate',
        'Chemical_Category': 'Metallic_Salt_Fatty_Acid',
        'Approval_Status': 'FDA_Approved',
        'Tg_C': 'Not_Applicable',
        'Hygroscopicity': 'Low',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Lubricant/Flow_Enhancer',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    {
        'Excipient_ID': 'EXC014',
        'Excipient_Name': 'Silicon_Dioxide',
        'Chemical_Category': 'Inorganic_Oxide',
        'Approval_Status': 'FDA_Approved',
        'Tg_C': 'Not_Applicable',
        'Hygroscopicity': 'Low',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Anti-Hygroscopic_Agent/Glidant',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    {
        'Excipient_ID': 'EXC015',
        'Excipient_Name': 'Titanium_Dioxide',
        'Chemical_Category': 'Inorganic_Oxide',
        'Approval_Status': 'FDA_Approved_Limited',
        'Tg_C': 'Not_Applicable',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Excipient',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    
    # SECTION 3: POTENTIAL NEW MATERIALS
    
    # Oligosaccharides
    {
        'Excipient_ID': 'EXC016',
        'Excipient_Name': 'Trehalose',
        'Chemical_Category': 'Oligosaccharide',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'High',
        'Hygroscopicity': 'Low',
        'Reducing_Character': 'No',
        'Primary_Function': 'Stabilizer/Carrier',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    {
        'Excipient_ID': 'EXC017',
        'Excipient_Name': 'Raffinose',
        'Chemical_Category': 'Oligosaccharide',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'High',
        'Reducing_Character': 'Not_Mentioned',
        'Primary_Function': 'Carrier',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    {
        'Excipient_ID': 'EXC018',
        'Excipient_Name': 'Cyclodextrins',
        'Chemical_Category': 'Oligosaccharide',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'No',
        'Primary_Function': 'Solubility_Enhancer/Stabilizer',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    {
        'Excipient_ID': 'EXC019',
        'Excipient_Name': 'Inulin',
        'Chemical_Category': 'Oligosaccharide',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'No',
        'Primary_Function': 'Bulking_Agent/Stabilizer',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    {
        'Excipient_ID': 'EXC020',
        'Excipient_Name': 'Sucrose',
        'Chemical_Category': 'Oligosaccharide',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'No',
        'Primary_Function': 'Stabilizer/Cryoprotectant',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    
    # Polysaccharides
    {
        'Excipient_ID': 'EXC021',
        'Excipient_Name': 'Pullulan',
        'Chemical_Category': 'Polysaccharide',
        'Approval_Status': 'Potential_New',
        'Tg_C': '261',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'No',
        'Primary_Function': 'Film_Former/Shell_Former',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    {
        'Excipient_ID': 'EXC022',
        'Excipient_Name': 'Dextran',
        'Chemical_Category': 'Polysaccharide',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'High',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'Not_Mentioned',
        'Primary_Function': 'Stabilizer/Mucopenetrator',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    {
        'Excipient_ID': 'EXC023',
        'Excipient_Name': 'Hyaluronic_Acid',
        'Chemical_Category': 'Polysaccharide',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Mucoadhesive/Targeting_Ligand',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Variable'
    },
    {
        'Excipient_ID': 'EXC024',
        'Excipient_Name': 'Chitosan',
        'Chemical_Category': 'Polysaccharide',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Mucoadhesive/Permeation_Enhancer',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Variable'
    },
    {
        'Excipient_ID': 'EXC025',
        'Excipient_Name': 'Fucoidan',
        'Chemical_Category': 'Polysaccharide',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Macrophage_Targeting/Antioxidant',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    {
        'Excipient_ID': 'EXC026',
        'Excipient_Name': 'Chondroitin_Sulfate',
        'Chemical_Category': 'Polysaccharide',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Macrophage_Targeting/CD44_Ligand',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    {
        'Excipient_ID': 'EXC027',
        'Excipient_Name': 'Alginate',
        'Chemical_Category': 'Polysaccharide',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Gelling_Agent/pH_Responsive',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Variable'
    },
    {
        'Excipient_ID': 'EXC028',
        'Excipient_Name': 'CMC',
        'Chemical_Category': 'Cellulose_Derivative',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'No',
        'Primary_Function': 'Mucoadhesive/Stabilizer',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    {
        'Excipient_ID': 'EXC029',
        'Excipient_Name': 'Galactomannan',
        'Chemical_Category': 'Polysaccharide',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'Not_Mentioned',
        'Primary_Function': 'Macrophage_Targeting',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    
    # Polyols
    {
        'Excipient_ID': 'EXC030',
        'Excipient_Name': 'Sorbitol',
        'Chemical_Category': 'Polyol',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'High',
        'Reducing_Character': 'No',
        'Primary_Function': 'Stabilizer',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    {
        'Excipient_ID': 'EXC031',
        'Excipient_Name': 'Erythritol',
        'Chemical_Category': 'Polyol',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'Low',
        'Reducing_Character': 'No',
        'Primary_Function': 'Stabilizer/Carrier',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    {
        'Excipient_ID': 'EXC032',
        'Excipient_Name': 'Xylitol',
        'Chemical_Category': 'Polyol',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'No',
        'Primary_Function': 'Antimicrobial/Mucolytic',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    
    # Amino Acids (New)
    {
        'Excipient_ID': 'EXC033',
        'Excipient_Name': 'L-Leucine',
        'Chemical_Category': 'Amino_Acid',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'Low',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Dispersibility_Enhancer',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': '0.25-1000_kDa'
    },
    {
        'Excipient_ID': 'EXC034',
        'Excipient_Name': 'Trileucine',
        'Chemical_Category': 'Amino_Acid',
        'Approval_Status': 'Potential_New',
        'Tg_C': '104',
        'Hygroscopicity': 'Low',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Dispersibility_Enhancer',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    
    # Lipids
    {
        'Excipient_ID': 'EXC035',
        'Excipient_Name': 'DPPC',
        'Chemical_Category': 'Phospholipid',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Shell_Former/Lung_Protective',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    {
        'Excipient_ID': 'EXC036',
        'Excipient_Name': 'Cholesterol',
        'Chemical_Category': 'Sterol',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'Not_Applicable',
        'Hygroscopicity': 'Low',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Membrane_Stabilizer',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    {
        'Excipient_ID': 'EXC037',
        'Excipient_Name': 'Tristearin',
        'Chemical_Category': 'Lipid',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'Not_Applicable',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Solid_Lipid_Matrix',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    {
        'Excipient_ID': 'EXC038',
        'Excipient_Name': 'Glycerol_Behanate',
        'Chemical_Category': 'Lipid',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'Not_Applicable',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Sustained_Release_Matrix',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Not_Mentioned'
    },
    
    # Synthetic Polymers
    {
        'Excipient_ID': 'EXC039',
        'Excipient_Name': 'PLGA',
        'Chemical_Category': 'Synthetic_Polymer',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'Variable',
        'Hygroscopicity': 'Low',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Sustained_Release_Carrier',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Variable'
    },
    {
        'Excipient_ID': 'EXC040',
        'Excipient_Name': 'PLA',
        'Chemical_Category': 'Synthetic_Polymer',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'Variable',
        'Hygroscopicity': 'Low',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Sustained_Release_Carrier',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Variable'
    },
    {
        'Excipient_ID': 'EXC041',
        'Excipient_Name': 'PEG',
        'Chemical_Category': 'Synthetic_Polymer',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'Variable',
        'Hygroscopicity': 'High',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Stealth_Coating/Mucopenetrator',
        'Melting_Point_Info': 'Variable',
        'Molecular_Weight_Info': 'Variable'
    },
    {
        'Excipient_ID': 'EXC042',
        'Excipient_Name': 'PVA',
        'Chemical_Category': 'Synthetic_Polymer',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'Not_Mentioned',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Mucoadhesive/Crystallization_Inhibitor',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Variable'
    },
    {
        'Excipient_ID': 'EXC043',
        'Excipient_Name': 'PCL',
        'Chemical_Category': 'Synthetic_Polymer',
        'Approval_Status': 'Potential_New',
        'Tg_C': 'Not_Mentioned',
        'Hygroscopicity': 'Low',
        'Reducing_Character': 'Not_Applicable',
        'Primary_Function': 'Sustained_Release_Carrier',
        'Melting_Point_Info': 'Not_Mentioned',
        'Molecular_Weight_Info': 'Variable'
    }
]

# Convert to DataFrame
for exc in excipients:
    for key in excipients_data.keys():
        excipients_data[key].append(exc[key])

df_excipients = pd.DataFrame(excipients_data)

# Save to CSV
df_excipients.to_csv('excipients_main.csv', index=False)
print(f"Extracted {len(df_excipients)} excipients to excipients_main.csv")
print("\nFirst 10 entries:")
print(df_excipients.head(10))
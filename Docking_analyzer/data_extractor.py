import urllib
import argparse
import pandas as pd
from bs4 import BeautifulSoup

def get_file (input_file=None,out_file=None,representation=None):
    input_file      = input ('type the name of the input file (format must be csv, and first column named entry):')
    out_file     = input ('type the name of the out file (format must be CSV):')
    representation = input ('type what you want (can be, smiles, cas, inchikey, inchi or synonyms):')
    df = pd.read_csv(input_file,encoding = "utf-8")
    saved_column = df.entry

    if representation == 'smiles':
        ENTRY=[]
        SMILES=[]
        for molecule in saved_column:
            smiles=getSMILES (molecule)
            ENTRY.append (molecule)
            SMILES.append (smiles)
            d={'User_Entry':pd.Series(ENTRY),
            'SMILES':pd.Series(SMILES)}
            table=pd.DataFrame (d)
        table.to_csv (out_file)

    if representation == 'cas':
        ENTRY=[]
        CAS=[]
        for molecule in saved_column:
            cas=getCAS (molecule)
            ENTRY.append (molecule)
            CAS.append (cas)
            d={'User_Entry':pd.Series(ENTRY),
            'CAS':pd.Series(CAS)}
            table=pd.DataFrame (d)
        table.to_csv (out_file)

    if representation == 'inchikey':
        ENTRY=[]
        Key=[]
        for molecule in saved_column:
            InChIKey=getInChIKey (molecule)
            ENTRY.append (molecule)
            Key.append (InChIKey)
            d={'User_Entry':pd.Series(ENTRY),
            'InChIKey':pd.Series(Key)}
            table=pd.DataFrame (d)
        table.to_csv (out_file)

    if representation == 'inchi':
        ENTRY=[]
        ChI=[]
        for molecule in saved_column:
            InChI=getInChI (molecule)
            ENTRY.append (molecule)
            ChI.append (InChI)
            d={'User_Entry':pd.Series(ENTRY),
            'InChI':pd.Series(ChI)}
            table=pd.DataFrame (d)
        table.to_csv (out_file)

    if representation == 'synonyms':
        ENTRY=[]
        Syn=[]
        for molecule in saved_column:
            syn=getSynonyms (molecule)
            ENTRY.append (molecule)
            Syn.append (syn)
            d={'User_Entry':pd.Series(ENTRY),
            'Synonyms':pd.Series(Syn)}
            table=pd.DataFrame (d)

        table.to_csv (out_file)

def getCAS (id):
    content = lookup (id,'cas')
    return content

def getSMILES (id):
    content = lookup (id, 'smiles')
    return content

def getInChIKey(id):
    content = lookup(id, 'stdinchikey')
    return content

def getInChI(id):
    content = lookup(id, 'stdinchi')
    return content

def getSynonyms(id):
    content = lookup(id, 'names')
    return content

def lookup (id, representation):
        url = 'https://cactus.nci.nih.gov/chemical/structure/' + id + '/' + representation
        with urllib.request.urlopen(url) as response:
            http = response.read()
            soup = BeautifulSoup(http,"html.parser")
            return soup

if __name__ == "__main__":
    get_file()#input_file=input_file,out_file=out_file,representation=representation)

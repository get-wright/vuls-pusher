import yaml

def load_config(config_path):
    with open(config_path, 'r') as config_file:
        return yaml.safe_load(config_file)
    
Azure_AD_Client_Secret: Va71Q~E_PSCZfR143Ks8GhaTsZ_RHneYPN6Y6Tc
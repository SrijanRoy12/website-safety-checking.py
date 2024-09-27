import random

# Mock function to simulate safety score
def get_safety_score(domain):
    # In reality, you'd call a web safety API like VirusTotal or Google Safe Browsing
    # This is a mock function that randomly assigns safety scores
    safety_score = random.randint(1, 100)
    if safety_score > 80:
        status = "Safe"
    elif safety_score > 50:
        status = "Moderately Safe"
    else:
        status = "Unsafe"
    
    return safety_score, status

# Function to evaluate website safety
def check_website_safety(domain):
    print(f"Checking safety for website: {domain}")
    
    safety_score, status = get_safety_score(domain)
    
    print(f"Website: {domain}")
    print(f"Safety Score: {safety_score}/100")
    print(f"Status: {status}")
    
    if status == "Unsafe":
        print("Warning: This website might be unsafe. Proceed with caution.")
    elif status == "Moderately Safe":
        print("This website has some potential risks. Use carefully.")
    else:
        print("This website is considered safe.")
    
    return safety_score, status

# Example usage
if __name__ == "__main__":
    website = input("Enter website URL: ")
    check_website_safety(website)

def analyze_complaint(complaint):
    """
    Analyze a sustainability complaint and return:
    category, subcategory, priority,
    sustainability area and summary.
    """

    text = complaint.lower().strip()

    # Default values
    category = "Other"
    subcategory = "General Environmental Issue"
    priority = "Medium"
    sustainability_area = "Environmental Sustainability"

    # -------------------------
    # Waste Management
    # -------------------------
    if any(word in text for word in [
        "garbage", "waste", "trash", "dump",
        "dumped", "litter", "plastic", "rubbish"
    ]):
        category = "Waste Management"

        if any(word in text for word in [
            "dump", "dumped", "illegal dumping"
        ]):
            subcategory = "Illegal Dumping"
            priority = "High"

        elif "plastic" in text:
            subcategory = "Plastic Waste"
            priority = "Medium"

        else:
            subcategory = "Improper Waste Disposal"
            priority = "Medium"

        sustainability_area = "Waste & Environmental Health"

    # -------------------------
    # Water & Sanitation
    # -------------------------
    elif any(word in text for word in [
        "water", "sewage", "sewer",
        "drain", "drainage", "toilet",
        "contamination", "contaminated"
    ]):
        category = "Water & Sanitation"

        if any(word in text for word in [
            "contamination", "contaminated",
            "sewage", "sewer"
        ]):
            subcategory = "Water Contamination"
            priority = "High"

        else:
            subcategory = "Water/Sanitation Issue"
            priority = "Medium"

        sustainability_area = "Water & Public Health"

    # -------------------------
    # Air & Noise Pollution
    # -------------------------
    elif any(word in text for word in [
        "smoke", "air pollution",
        "pollution", "dust", "noise",
        "loud", "sound"
    ]):
        category = "Air & Noise Pollution"

        if any(word in text for word in [
            "smoke", "air pollution", "dust"
        ]):
            subcategory = "Air Pollution"

        else:
            subcategory = "Noise Pollution"

        priority = "High"
        sustainability_area = "Clean Air & Healthy Communities"

        # -------------------------
    # Energy & Infrastructure
    # -------------------------
    elif any(word in text for word in [
        "street light",
        "street lights",
        "electricity",
        "energy",
        "solar",
        "road",
        "infrastructure"
    ]):
        category = "Energy & Infrastructure"
        subcategory = "Infrastructure Issue"
        priority = "Medium"
        sustainability_area = "Sustainable Infrastructure"


    # -------------------------
    # Green Environment
    # -------------------------
    elif any(word in text.split() for word in [
        "tree",
        "trees",
        "deforestation",
        "park",
        "forest",
        "greenery",
        "plant"
    ]):
        category = "Green Environment"
        subcategory = "Green Space / Vegetation Issue"
        priority = "Medium"
        sustainability_area = "Biodiversity & Green Environment"

    # -------------------------
    # Summary
    # -------------------------
    summary = complaint.strip()

    if len(summary) > 150:
        summary = summary[:147] + "..."

    return {
        "category": category,
        "subcategory": subcategory,
        "priority": priority,
        "sustainability_area": sustainability_area,
        "summary": summary
    }


# -------------------------
# Test the AI Analyzer
# -------------------------

if __name__ == "__main__":

    complaints = [
        "There is garbage dumped near our lake.",
        "The drinking water in our area is contaminated.",
        "A factory is releasing thick smoke into the air.",
        "People are cutting down trees near the park.",
        "Street lights are not working in our area."
    ]

    for complaint in complaints:

        result = analyze_complaint(complaint)

        print("\nComplaint:", complaint)
        print("Category:", result["category"])
        print("Subcategory:", result["subcategory"])
        print("Priority:", result["priority"])
        print("Sustainability Area:", result["sustainability_area"])
        print("Summary:", result["summary"])
        print("-" * 50)
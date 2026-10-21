def split_budget(income):
    """Split monthly income using the 50/30/20 rule."""
    needs = income * 0.50
    wants = income * 0.30
    savings = income * 0.20
    return {"needs": needs, "wants": wants, "savings": savings}

if __name__ == "__main__":
    print(split_budget(3000))
def select_patients(patients, k):
    """
    Select up to k patient names in the order they should be called.

    Patients are dictionaries with:
      - "name": string
      - "severity": integer 1 (most urgent) to 5 (least urgent)
      - "arrival_order": integer, smaller means arrived earlier

    Priority rules:
      1. Lower severity number first.
      2. If severity ties, lower arrival_order first.

    Return a list of names in the correct order.
    """

    # If no patients or k == 0, return empty list
    if k <= 0 or not patients:
        return []

    # Sort using a stable sort: first by severity, then arrival_order
    sorted_patients = sorted(
        patients,
        key=lambda p: (p["severity"], p["arrival_order"])
    )

    # Select the top k names
    result = [p["name"] for p in sorted_patients[:k]]

    return result


if __name__ == "__main__":
    sample_patients = [
        {"name": "Alex", "severity": 3, "arrival_order": 5},
        {"name": "Bella", "severity": 1, "arrival_order": 6},
        {"name": "Chris", "severity": 1, "arrival_order": 2},
    ]
    print(select_patients(sample_patients, 2))

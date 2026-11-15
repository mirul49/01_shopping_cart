# Shop Order Calculation — Test Case Specification

## Scope

Verify `calculate_total(unit_price_cents, quantity)` and
`qualifies_free_delivery(total_cents)` against the shopping cart specification.
All monetary values are integer Singapore cents. The functions are tested
independently.

## Test cases

| ID | Function | Input | Expected result |
|---|---|---|---|
| CT-01 | `calculate_total` | Price 250, quantity 3 | Returns 750 |
| CT-02 | `calculate_total` | Price 0, quantity 3 | Returns 0 |
| CT-03 | `calculate_total` | Price 250, quantity 0 | Returns 0 |
| CT-04 | `calculate_total` | Boolean, float, or string argument | Raises `TypeError` |
| CT-05 | `calculate_total` | Negative price or quantity | Raises `ValueError` |
| FD-01 | `qualifies_free_delivery` | Total 4999 | Returns `False` |
| FD-02 | `qualifies_free_delivery` | Total 5000 | Returns `True` |
| FD-03 | `qualifies_free_delivery` | Total 5001 | Returns `True` |
| FD-04 | `qualifies_free_delivery` | Boolean, float, or string total | Raises `TypeError` |
| FD-05 | `qualifies_free_delivery` | Negative total | Raises `ValueError` |

## Troubleshooting notes

- **CT-03 exposed Error 1:** `max(quantity, 1)` changed a valid quantity of zero
  into one, so the function returned the unit price rather than zero. Multiplying
  by the validated quantity directly fixes the calculation.
- **FD-02 exposed Error 2:** `total_cents > 5000` excluded the exact S$50.00
  threshold. The requirement says “S$50.00 or more”, so the comparison must be
  `>= 5000`.
- If an invalid-input test fails, check that type validation runs before range
  validation and that booleans are rejected (`bool` is a subclass of `int` in
  Python).

Run the cases from the project folder with `python -m pytest -q`.

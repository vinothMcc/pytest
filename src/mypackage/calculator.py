from flask import Flask

def add(a, b):
    """Return the sum of ``a`` and ``b``.

    Parameters
    ----------
    a : int | float
        First addend.
    b : int | float
        Second addend.

    Returns
    -------
    int | float
        The numeric sum of ``a`` and ``b``.
    """
    # Perform numeric addition and return the result.
    return a + b

def divide(a, b):
    print("divide called")
    """Return the division of a by b."""
    if b == 0:
        print("Cannot divide by zero")
        raise ValueError("Cannot divide by zero")
    return a / b

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok"}
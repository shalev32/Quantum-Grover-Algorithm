"""
Setup script for IBM Quantum credentials.

Run this script to save your IBM Quantum API token.
You only need to run this once.
"""

from qiskit_ibm_runtime import QiskitRuntimeService

def setup_ibm_quantum():
    """
    Interactive setup for IBM Quantum credentials.
    """
    print("=" * 60)
    print("IBM Quantum Setup")
    print("=" * 60)
    print()
    print("To get your API token:")
    print("1. Go to https://quantum.cloud.ibm.com/")
    print("2. Log in or create a free account")
    print("3. Click on your profile icon and select 'Account settings'")
    print("4. Copy your API token from the 'API tokens' section")
    print()
    
    token = input("Enter your IBM Quantum API token: ").strip()
    
    if not token:
        print("Error: Token cannot be empty")
        return False
    
    try:
        # Save the account
        QiskitRuntimeService.save_account(
            channel="ibm_quantum_platform",
            token=token,
            overwrite=True
        )
        print()
        print("✓ Token saved successfully!")
        print()
        
        # Test the connection
        print("Testing connection...")
        service = QiskitRuntimeService()
        backends = service.backends()
        
        print(f"✓ Connection successful!")
        print(f"✓ You have access to {len(list(backends))} quantum backends")
        print()
        print("You're all set! You can now run the notebooks with QPU access.")
        return True
        
    except Exception as e:
        print()
        print(f"✗ Error: {e}")
        print()
        print("Please check your token and try again.")
        return False


if __name__ == "__main__":
    setup_ibm_quantum()

import streamlit as st
st.set_option("gatherUsageStats", False)

def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
def main():
    st.title("Find the Largest Number")
    st.write("Enter three numbers below:")
    
    a = st.number_input("Enter the first number:")
    b = st.number_input("Enter the second number:")
    c = st.number_input("Enter the third number:")
    
    if st.button("Find the Largest Number"):
        result = find_largest(a, b, c)
        st.write("The largest number is:", result)
        
if __name__ == "__main__":
    main()

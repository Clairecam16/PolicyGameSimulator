import streamlit as st

def display_educational_content():
    """
    Displays educational content about fiscal policy and Nash Equilibrium
    """
    st.header("📚 Learning Center")

    st.subheader("What is Fiscal Policy?")
    st.write("""
    Fiscal policy refers to government spending and taxation decisions that influence the economy.

    **Key concepts:**
    - 🏦 **Austerity**: Reducing government spending and increasing taxes
    - 💰 **Stimulus**: Increasing government spending and reducing taxes
    """)

    st.subheader("Understanding Nash Equilibrium")
    st.write("""
    A Nash Equilibrium occurs when no player can benefit by changing their strategy unilaterally.

    The optimal strategy depends on the economic scenario:
    - During a **crisis**, coordinated stimulus might be better
    - During **inflation**, coordinated austerity might be preferred
    - During **recovery**, mixed strategies might emerge
    """)

    st.subheader("Real-World Applications")
    st.write("""
    Historical examples of policy coordination:

    1. **2008 Financial Crisis**
    - Many countries implemented stimulus packages
    - Some European nations chose austerity

    2. **1970s Stagflation**
    - High inflation led to coordinated monetary tightening
    - Mixed fiscal responses between nations

    3. **Post-WW2 Recovery**
    - Marshall Plan provided coordinated stimulus
    - Successful international cooperation
    """)

    st.subheader("Tips for Playing")
    st.write("""
    1. Consider the current economic scenario
    2. Anticipate the AI's likely response
    3. Think about long-term consequences
    4. Look for Nash Equilibrium opportunities
    5. Learn from historical examples
    """)
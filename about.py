import  streamlit as st

def app():
    st.header(":orange[The Fish Farming Experts!]")
   # st.subheader(":orange[More on the Chatbot...]")
    
    
    st.write("Fish farming, also known as aquaculture, is the practice of raising fish in enclosures such as ponds, tanks, or net pens, usually for food, sport, or aquarium trade. This method has become increasingly important as global demand for seafood continues to rise, putting pressure on wild fish populations. Fish farming allows for the efficient production of fish, ensuring a stable supply of seafood without overfishing natural populations.")

    
    
    st.subheader(":orange[Issues Faced by Fish Farmers Regarding Correct and Accurate Readings]")
    
    st.write("One of the major challenges in fish farming is maintaining the optimal conditions for the health and growth of fish. This requires accurate and timely readings of various environmental parameters, including water temperature, pH levels, oxygen levels, and the presence of potential contaminants. Incorrect or inaccurate readings can lead to several problems, such as:")
    
    col1, col2, col3= st.columns([1, 1, 1]) 
    
    bullet1 = """
        - Poor Water Quality: Without accurate measurements, farmers may not be able to maintain the water quality required for fish health, leading to disease outbreaks or even mass die-offs.
        """
        
    bullet2 = """
        - Inefficient Feeding Practices: Lack of precise data can result in over or underfeeding, leading to waste of resources and potential pollution.
        """
        
    bullet3 = """
        - Growth and Health Issues: Incorrect readings of water conditions can affect the growth rate and overall health of the fish, impacting their market value and the profitability of the farm.
        """
        
    bullet4 = """
        - Regulatory Compliance: Fish farms often have to meet certain environmental standards. Inaccuracies in monitoring can lead to non-compliance, resulting in fines or shutdowns.
        """
    
    with col1:
        
    
        st.write(bullet1)        
    
    with col2:
        st.write(bullet2)
    
        st.write(bullet3)
        
    with col3:
        
        st.write(bullet4)
    
    st.subheader(":orange[The Importance of \"The Fish Farming Expert\" Chatbot]")
        
    st.write("\"The Fish Farming Expert\" chatbot emerges as a pivotal tool in addressing these challenges. This chatbot serves as a virtual assistant to fish farmers, offering several significant advantages:")
        
    st.write("Real-time Assistance: It can provide fish farmers with real-time advice and alerts regarding the optimal conditions needed for their fish, helping them make immediate adjustments to the environment.")
    
    st.write("Data Accuracy: By integrating with various sensors and data sources, the chatbot can analyze and interpret accurate readings, ensuring that the farmers receive the most current and precise information.")
    
    st.write("Decision Support: The chatbot can help in decision-making processes by suggesting the best courses of action based on the data collected. For instance, it might recommend adjusting feed types or quantities in response to water temperature changes.")
    
    st.write("Ease of Use: Designed to be user-friendly, the chatbot allows farmers, regardless of their technical expertise, to access complex data analytics in a straightforward manner. This accessibility is crucial for widespread adoption and effective use.")
    
    st.write("Educational Resource: Beyond immediate problem-solving, the chatbot can serve as an educational tool, providing farmers with ongoing learning opportunities about best practices in fish farming.")
    
    st.write("")
  
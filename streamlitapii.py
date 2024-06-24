import pickle
import streamlit as st

mdl = pickle.load(open('C:/Users/JOAN/OneDrive/Desktop/ML_PROJECT_1/svr_model.pkl', 'rb'))

def main():
    st.title('Gadgets Pricing prediction Solution')
    
    #input variables
    prices = {}
    prices['isSale'] = st.text_input('isSale')
    weight = st.text_input('weight')
    prices['available'] = st.text_input('available')
    prices['availability_FALSE'] = st.text_input('availability_FALSE')
    prices['availability_In_Stock']= st.text_input('availability_In_Stock')
    prices['availability_More_on_the_Way'] = st.text_input('availability_More_on_the Way')
    prices['availability_No'] = st.text_input('availability_No')
    prices['availability_Out_Of_Stock'] = st.text_input('availability_Out_Of_Stock')
    prices['availability_Retired'] = st.text_input('availability_Retired')
    prices['availability_Special_Order']= st.text_input('availability_Special_Order')
    prices['availability_TRUE'] = st.text_input('availability_TRUE')
    prices['availability_Yes']= st.text_input('availability_Yes')
    prices['availability_sold'] = st.text_input('availability_sold')
    prices['availability_undefined'] = st.text_input('availability_undefined')
    prices['availability_yes'] = st.text_input('availability_yes')
    prices['primaryCategories_Apple_CarPlay'] = st.text_input('primaryCategories_Apple_CarPlay')
    prices['primaryCategories_Intel_Celeron'] = st.text_input('primaryCategories_Intel_Celeron')
    prices['primaryCategories_SiriEyesFree'] = st.text_input('primaryCategories_SiriEyesFree')
    prices['primaryCategories_Electronics'] = st.text_input('primaryCategories_Electronics')
    prices['primaryCategories_Electronics,Furniture'] = st.text_input('primaryCategories_Electronics,Furniture')
    prices['condition_New'] = st.text_input('condition_New')
    prices['condition_New_other'] = st.text_input('condition_New_other')
    prices['condition_Refurbished ']  = st.text_input('condition_Refurbished ')
    prices['condition_Seller_refurbished'] = st.text_input('condition_Seller_refurbished')
    prices['condition_Used']= st.text_input('condition_Used')
    prices['condition_new'] = st.text_input('condition_new')
    prices['condition_pre_owned'] = st.text_input('condition_pre_owned')
    prices['condition_refurbished']= st.text_input('condition_refurbished')
    prices['currency_CAD'] = st.text_input('currency_CAD')
    prices['currency_USD'] = st.text_input('currency_USD')
    
    
    #display collected inputs
    st.write('Collected Input Values: ', prices)
    
    #prediction code
    if st.button('Predict'):
        makeprediction = mdl.predict([[prices['isSale'], weight, prices['available'], prices['availability_FALSE'], prices['availability_In_Stock'], prices['availability_More_on_the_Way'], prices['availability_No'], prices['availability_Out_Of_Stock'], prices['availability_Retired'], prices['availability_Special_Order'], prices['availability_TRUE'], prices['availability_Yes'], prices['availability_sold'], prices['availability_undefined'], prices['availability_yes'], prices['primaryCategories_Apple_CarPlay'], prices['primaryCategories_Intel_Celeron'], prices['primaryCategories_SiriEyesFree'], prices['primaryCategories_Electronics'], prices['primaryCategories_Electronics,Furniture'], prices['condition_New'], prices['condition_New_other'], prices['condition_Refurbished '], prices['condition_Seller_refurbished'], prices['condition_Used, prices.condition_new'], prices['condition_pre_owned'], prices['condition_refurbished'], prices['currency_CAD'], prices['currency_USD']]]) 
        output = round(makeprediction[0], 2)
        st.success('You can buy the gadget for {}'.format(output))
        
        
if __name__ =='__main__':
    main()
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from BASIC import basic
from LOAN import loan
from CPEQ import cpeq

basic=basic()



def check_int(n,j):
    # print(f"n {n}     j: {j}")
    try:
        n=float(n)
        j=float(j)
        return True
    except:
        st.warning("input must be digit")
        return False

    # if (not n.isdigit()) or (not j.isdigit()):
    #     if not n.isdigit():
    #         st.warning("n has to be a digit ")
    #     if not j.isdigit():
    #         st.warning("j has to be a digit ")
    #     return False

    # else:
    #    return True




an_Image=Image.open("notation/an.png")
sn_Image=Image.open("notation/sn.png")
an_dd_Image=Image.open("notation/an_dd.png")
sn_dd_Image=Image.open("notation/sn_dd.png")
#
Ia_Image=Image.open("notation/Ia.png")
Is_Image=Image.open("notation/Is.png")

#
Da_Image=Image.open("notation/Da.png")
Ds_Image=Image.open("notation/Ds.png")



with st.beta_expander("Basic"):
#
    st.markdown("<center><font size =7 center> Annuity Immediate </font></center>", unsafe_allow_html=True)
    left_column, middle_col,right_column = st.beta_columns(3)
    suba1, suba2 , suba3, suba4, suba5, suba6, suba7, suba8= st.beta_columns(8)
    subaa1, subaa2 , subaa3, subaa4, subaa5, subaa6= st.beta_columns(6)
    sub_left_column, sub_middle_col, sub_right_column = st.beta_columns(3)


    # You can use a column just like st.sidebar:

    with left_column:
        st.image(an_Image, width=100)
        
        a1_n=suba1.text_input(" n")
        a1_j=suba2.text_input(" j")
        start_a1=suba3.button("compute")
        if start_a1:
            if check_int(a1_n,a1_j):
                print(f"check int {check_int}")
                #out put
                basic.an_value= " `"+ str(basic.an(float(a1_n), float(a1_j)))+"`"
                # sub_left_column.markdown("#### res: " + " `"+ str(basic.an(float(a1_n), float(a1_j)))+"`")
        
        sub_left_column.markdown("#### res: "+basic.an_value)



    with right_column:
        
        st.image(sn_Image, width=100)
        a2_n=suba6.text_input("n for sn", key="a2_1")
        a2_j=suba7.text_input("j for sn", key="a2_2")
        start_a2=suba8.button("compute", key="a2_3")
        if start_a2:
            if check_int(a2_n,a2_j):
                #out put
                sub_right_column.markdown("#### res: " + " `"+ str(basic.sn(float(a2_n), float(a2_j)))+"`")
        # else:
        #     sub_right_column.markdown("#### res: ")

    st.markdown("---")
    ######################

    st.markdown("<center><font size =7 center> Annuity Due </font></center>", unsafe_allow_html=True)


    b1,b2,b3 = st.beta_columns(3)
    sub_b1, sub_b2 , sub_b3, sub_b4, sub_b5, sub_b6, sub_b7, sub_b8= st.beta_columns(8)
    sub_left_column, sub_middle_col, sub_right_column = st.beta_columns(3)

    with b1:
        st.image(an_dd_Image, width=100)
        
        b1_n=sub_b1.text_input(" n", key="b1_1")
        b1_j=sub_b2.text_input(" j", key="b1_2")
        start_b1=sub_b3.button("compute", key="b1_button")
        if start_b1:
            if check_int(b1_n,b1_j):
                print(f"check int {check_int}")
                #out put
                basic.an_due_value= " `"+ str(basic.an_due(float(b1_n), float(b1_j)))+"`"
                # sub_left_column.markdown("#### res: " + " `"+ str(basic.an(float(a1_n), float(a1_j)))+"`")
        sub_left_column.markdown("#### res: "+basic.an_due_value)

    with b3:
        st.image(sn_dd_Image, width=100)
        b2_n=sub_b6.text_input("n for sn", key="b2_1")
        b2_j=sub_b7.text_input("j for sn", key="b2_2")
        start_b2=sub_b8.button("compute", key="b2_3")
        if start_b2:
            if check_int(b2_n,b2_j):
                #out put
                sub_right_column.markdown("#### res: " + " `"+ str(basic.sn(float(b2_n), float(b2_j)))+"`")

    ##############################################
    st.markdown("---")
    st.markdown("<center><font size =7 center> Arithmetic Progression  </font></center>", unsafe_allow_html=True)
    st.markdown(" &nbsp", unsafe_allow_html=True)


    c1,c2,c3 = st.beta_columns(3)
    sub_c1, sub_c2 , sub_c3, sub_c4, sub_c5, sub_c6, sub_c7, sub_c8= st.beta_columns(8)
    sub_left_column, sub_middle_col, sub_right_column = st.beta_columns(3)
    st.markdown("---")


    with c1:
        st.image(Ia_Image, width=100)
        c1_n=sub_c1.text_input(" n", key="c1_1")
        c1_j=sub_c2.text_input(" j", key="c1_2")
        start_c1=sub_c3.button("compute", key="c1_button")
        if start_c1:
            if check_int(c1_n,c1_j):
                print(f"check int {check_int}")
                #out put
                basic.Ia_value= " `"+ str(basic.IS(float(c1_n), float(c1_j)))+"`"
                # sub_left_column.markdown("#### res: " + " `"+ str(basic.an(float(a1_n), float(a1_j)))+"`")
        sub_left_column.markdown("#### res: "+basic.Ia_value)
        # print(f"IA {basic.Ia_value}")

    with c3:
        st.image(sn_dd_Image, width=100)
        c2_n=sub_c6.text_input("n for sn", key="c2_1")
        c2_j=sub_c7.text_input("j for sn", key="c2_2")
        start_c2=sub_c8.button("compute", key="c2_3")
        if start_c2:
            if check_int(c2_n,c2_j):
                #out put
                sub_right_column.markdown("#### res: " + " `"+ str(basic.sn(float(c2_n), float(c2_j)))+"`")

##############################################

    d1,d2,d3 = st.beta_columns(3)
    sub_d1, sub_d2 , sub_d3, sub_d4, sub_d5, sub_d6, sub_d7, sub_d8= st.beta_columns(8)
    sub_left_column, sub_middle_col, sub_right_column = st.beta_columns(3)
    st.markdown("---")


    with d1:
        st.image(Da_Image, width=100)
        d1_n=sub_d1.text_input(" n", key="d1_1")
        d1_j=sub_d2.text_input(" j", key="d1_2")
        start_d1=sub_d3.button("compute", key="d1_button")
        if start_d1:
            if check_int(d1_n,d1_j):
                print(f"check int {check_int}")
                #out put
                basic.Ia_value= " `"+ str(basic.IS(float(d1_n), float(d1_j)))+"`"
                # sub_left_column.markdown("#### res: " + " `"+ str(basic.an(float(a1_n), float(a1_j)))+"`")
        sub_left_column.markdown("#### res: "+basic.Ia_value)
        # print(f"IA {basic.Ia_value}")

    with d3:
        st.image(Ds_Image, width=100)
        d2_n=sub_d6.text_input("n for sn", key="d2_1")
        d2_j=sub_d7.text_input("j for sn", key="d2_2")
        start_d2=sub_d8.button("compute", key="d2_3")
        if start_d2:
            if check_int(d2_n,d2_j):
                #out put
                sub_right_column.markdown("#### res: " + " `"+ str(basic.sn(float(d2_n), float(d2_j)))+"`")



with st.beta_expander("Loan"):

    l1_header, l2_header=st.beta_columns(2)
    l1,l2,l3 = st.beta_columns(3)
    sub_l1, sub_l2 , sub_l3, sub_l4, sub_l5, sub_l6, sub_l7, sub_l8= st.beta_columns(8)
    sub_left_column, sub_middle_col, sub_right_column = st.beta_columns(3)

    l1_header.markdown("<font size =7 > input i,t,n,K  </font>", unsafe_allow_html=True)
    l2_header.markdown("<font size =7 > Result at time t </font>", unsafe_allow_html=True)
    st.markdown("---")

    i_value=l1.text_input("interest rate", key="i_value")
    t_value=l1.text_input("t (\"t\"th term)", key="t_value")
    n_value=l1.text_input("n (total num of terms)", key="n_value")
    k_value=l1.text_input("k (payment amount)", key="k_value")
    l_start=l1.button("compute", key="l")
    

    def check_int_loan(i_value,t_value,n_value,k_value):
        try:
            i_value=float(i_value)
            t_value=float(t_value)
            n_value=float(n_value)
            k_value=float(k_value)
            return True
        except:
            st.warning("all inputs must be digits")
            return False


    #res
    
    if l_start:
        if check_int_loan(i_value,t_value,n_value,k_value):
            loan=loan(i_value,t_value,n_value,k_value)
            loan.OB()
            loan.Pr()
            loan.It()
            print(loan.It_value)
        else:
            loan=loan()
    else:
        loan=loan()

    with l3:
        st.write("<font size =5 > Principle payment   </font>", unsafe_allow_html=True)
        st.write(loan.Pr_value)
        st.write("<br />", unsafe_allow_html=True)
        

        st.write("<font size =5 > Outstanding Balance   </font>", unsafe_allow_html=True)
        st.write(loan.OB_value)

        st.write("<br />", unsafe_allow_html=True)

        st.write("<font size =5 > Interest   </font>", unsafe_allow_html=True)
        st.write(loan.It_value)
        st.write("<br />", unsafe_allow_html=True)

#
# def check_int_cpeq(F_value,C_value,P_value,r_value,j_value,n_value):
#         try:
#             F_value=float(F_value)
#             C_value=float(C_value)
#             P_value=float(P_value)
#             r_value=float(r_value)
#             j_value=float(j_value)
#             n_value=float(n_value)
#             return True
#         except:
#             st.warning("all inputs must be digits")
#             return False

with st.beta_expander("Coupon Equation"):

    st.write("<font size =5 > Coupon Price Equation   </font>", unsafe_allow_html=True)

    cp1,cp2 = st.beta_columns(2)

    with cp1:
        F_value=st.text_input("Face value (F)", key="F_value")
        C_value=st.text_input("Redemption amount (C)", key="C_value")
        P_value=st.text_input("Coupon Price (P)", key="P_value")

    with cp2:
        r_value=st.text_input("Coupon Rate per coupon period (r)", key="r_value")
        j_value=st.text_input("Yeild Rate per coupon period (j)", key="j_value")
        n_value=st.text_input("number of coupon period (n)", key="n_value")


    
    cpeq_start=st.button("compute", key="cpeq")

    cpeq=cpeq()
    var_list=["F_value","C_value","P_value","r_value","j_value","n_value"]
    input_list=[F_value,C_value,P_value,r_value,j_value,n_value]
    str_list=["F", "C", "P", "r", "j", "n"]

    res_header_slot=st.empty()
    res_slot=st.empty()
    if cpeq_start:
        for i in range(len(var_list)):
            if input_list[i]=="":
                input_list[i]=str_list[i]
                st.warning(var_list[i]+ "is not given")
        
        cpeq.res=cpeq.eq(input_list)
        
    res_header_slot.markdown("<font size =4 > Result   </font>", unsafe_allow_html=True)
    res_slot.markdown(cpeq.res)
    st.write("<br />", unsafe_allow_html=True)

   
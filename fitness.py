import streamlit as st
st.set_page_config(page_title="FITNESS APP")
st.header("FITNESS APP")
Height = float(st.number_input("What is Your Height(centimeters)?: ",key=None))
Height = Height/100
Weight = float(st.number_input("What is Your Weight(kilograms)?: ",key=None))
if Height == 0:
     Height = 0.1
x = Weight/(Height*Height)
submit=st.button("Tell me ")

if submit:
    st.write("Your BMI is :", x)
    if x < 18.5:
        st.write("You are Underweight, Here are some tips to gain weight in a good way")
        st.write("""Eating more frequently. Slowly begin to eat 5 to 6 smaller meals during the day. Try to tune into your body to recognize when you might be hungry. But you may need to plan times to eat even if you aren't that hungry.
Choosing food with lots of nutrients. Set up a routine to eat and drink things you like and that have a lot of nutrients as well as calories. Talk with your health care provider or dietitian about how many calories to eat a day or in each meal. You also can ask how many servings you should eat of the different food groups.
Top it off. Add extras to your dishes for more calories, such as cheese in casseroles or nut butter on whole-grain toast. You also can add dry milk or liquid milk to foods for extra protein and calories. Some examples are mashed potatoes or soups.
Try smoothies and shakes. Avoid beverages with few nutrients or calories, such as diet soda. But a blend of high-calorie, nutritious ingredients in a smoothie or shake can help if you're eating on the go. Meal replacement drinks also may be part of your weight-gain effort.
But watch what and when you drink. Beverages can make you feel full. If that's the case for you, avoid drinking during a meal or before. But make sure you are drinking enough throughout the day.
Exercise. Exercise, especially strength training, can help you gain weight by building up your muscles. Exercise also may stimulate your appetite.""")
    if x > 18.5 and x <30:
        st.write("You are Normal, Here are some tips to maintain you body in this state")
        st.write(""" Eat smaller meals. Eating 5 small meals a day rather than 3 large ones can keep your metabolism working longer, helping you control your weight. Include metabolism-boosting spices like cinnamon, nutmeg, and turmeric.
        Stop eating when you’re full. You don’t need to finish everything on your plate just because it’s there. Even if there are leftovers, stop eating when you feel satiated.
Stick to healthy snacks. If you get hungry between meals, don’t go back to old habits of snacking on high-calorie snacks. Stick to healthier options like fruit, vegetables, fat-free yogurt, and whole wheat crackers.
Stay hydrated. Drinking 8 glasses of water a day not only helps you burn calories by keeping your metabolism going, it also quenches your thirst faster and better than anything else, especially diet diet sodas and sugary drinks.
""")
    if x >=30:
        st.write("You are Obese, Here are some tips to reduce your weight")
        st.write(""" Eat smaller meals. Eating 5 small meals a day rather than 3 large ones can keep your metabolism working longer, helping you control your weight. Include metabolism-boosting spices like cinnamon, nutmeg, and turmeric.
        Stop eating when you’re full. You don’t need to finish everything on your plate just because it’s there. Even if there are leftovers, stop eating when you feel satiated.
Stick to healthy snacks. If you get hungry between meals, don’t go back to old habits of snacking on high-calorie snacks. Stick to healthier options like fruit, vegetables, fat-free yogurt, and whole wheat crackers.
Stay hydrated. Drinking 8 glasses of water a day not only helps you burn calories by keeping your metabolism going, it also quenches your thirst faster and better than anything else, especially diet diet sodas and sugary drinks.
""")

import React from "react";
import { NavigationContainer } from '@react-navigation/native';
import HomeScreen from "../screens/HomeScreen/HomeScreen";
import AboutScreen from "../screens/AboutScreen/AboutScreen";
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import CommentsSreeen from "../screens/CommentsScreen/CommentsScreen";


export default function TabDrawer (){
    const Tab = createBottomTabNavigator();

    return (
        <NavigationContainer initialRouteName="Home">
            <Tab.Navigator >
                <Tab.Screen name="Home" component={HomeScreen} />
                <Tab.Screen name="Settings" component={AboutScreen} />
                <Tab.Screen name="Comments" component={CommentsSreeen} />
            </Tab.Navigator>
        </NavigationContainer>

        
    )
}


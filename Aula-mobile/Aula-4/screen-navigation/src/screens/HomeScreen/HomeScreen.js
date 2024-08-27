import React from "react";
import { View, Text, Button } from "react-native";

export default function HomeScreen ({ navigation }){
    const handlerAbout = () => navigation.navigate('About')
    return (
        <View>
            <Text> HomeScreen </Text>
            <Button title="About" onPress={handlerAbout}/> 
        </View>
    )
}
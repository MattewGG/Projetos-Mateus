import { StatusBar } from 'expo-status-bar';
import React, {useState}  from 'react';
import { Alert, StyleSheet, Text, TextInput, TouchableHighlight, TouchableOpacity, View } from 'react-native';
import api from './api';

export default function App() {
  const [cep, setCep ] = useState("")
  const [logradouro, setLogradouro] = useState("")
  const [bairro, setBairro] = useState("")
  const [localidade, setLocalidade] = useState("")
  const [uf, setUf]= useState("")
  function buacarCep(){
    if(cep == ""){
      Alert.alert("Cep invalido")
       setCep("")
      
    }
  }

  


  return (
    <View style={styles.container}>
        <View style={styles.nav}>
          <Text style={styles.title}><h1>Buscador de cep</h1></Text>


        </View>
        <View style={styles.cep} >
          <TextInput style={styles.input} 
           
            value={cep} 
            onChangeText={(texto) => setCep(texto)}
            placeholder='cep' />
            <TouchableOpacity>
              <Text>Buscar</Text>
            </TouchableOpacity>
        </View>
        <TextInput style={styles.caixas} 
           
           value={logradouro} 
           onChangeText={(texto) => setLogradouro(texto)}
           placeholder='Logradouro' />
         <TextInput style={styles.caixas} 
           
           value={bairro} 
           onChangeText={(texto) => setBairro(texto)}
           placeholder='Bairro' />
          <TextInput style={styles.caixas} 
           
           value={localidade} 
           onChangeText={(texto) => setLocalidade(texto)}
           placeholder='Localidade' />     

            <TextInput  style={styles.uf}
           
           value={uf} 
           onChangeText={(texto) => setUf(texto)}
           placeholder='uf' />     
    
      
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'column'
  },
  nav: {
   flexDirection: "row",
   height: 50,
  },
  title: {
    height: 30,
  },
  cep: {
    flexDirection: "row",
    height: 100,
    marginHorizontal: 20,
    backgraundColor: "blue"
  },
  input:{
    borderColor: "red",
    borderWidth: 2,
  },

  caixas:{
    borderColor:"#000000",
    borderWidth: 2,
    padding: 15,
    fontSize: 18,
    borderRadius: 10,
    marginTop: 20,
    marginEnd: 20,

  },
  uf:{
    width: 50, 
    height: 50,
    marginTop: 10,
    marginEnd: 20,
    borderColor: "red",
    borderWidth: 2,
  }
});

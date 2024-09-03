
import React from "react";

import { QueryClient, QueryClientProvider } from "react-query";

// navegacao:
import StackNavigator from "./src/navigation/StackNavigator";
import DrawerNavigator from "./src/navigation/DrawerNavigator";
import TabDrawer from "./src/navigation/TabDrawer";

const queryClient = new  QueryClient()

export default function App() {
  return (

    // nosso aplicativo esta sendo gerenciado pelo query client provider e por isso as coisas estao dentro dele 
    <QueryClientProvider client={queryClient}>
      <TabDrawer/>
    </QueryClientProvider>
 
    
  )
}


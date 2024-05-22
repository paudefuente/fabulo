/*


*/

// Libraries
import React, { useEffect, useState} from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { RootStackParamList } from './navigations/types';

import InboxScreen from './screens/Home/InboxScreen';
import Splash from 'react-native-splash-screen';
import { StackNavigationProp } from '@react-navigation/stack'; // Import the StackNavigationProp type from the @react-navigation/stack package
import { View } from 'react-native';

const Stack = createStackNavigator<RootStackParamList>();

const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        setTimeout(() => {
            setIsLoading(false);
        }, 2000);
    }, []);


 // if (isLoading) {
    //     return <Splash/>;
    // }

const Router: React.FC = () => {
    return (
        <View>
            <View>
            </View>
        </View>
    );
};

export default Router;
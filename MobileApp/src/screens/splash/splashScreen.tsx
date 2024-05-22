// Libraries 
import React, {useEffect} from 'react';
import {View, Image, StyleSheet} from 'react-native';
import SplashScreen from 'react-native-splash-screen';

const Splash: React.FC = () => {

    useEffect(() => {
        setTimeout(() => {
            SplashScreen.hide();
        }, 2000);
    }, [])

    return (
        <View style={styles.container}>
            <Image source={require('../../assets/images/splashScreen.jpg')} style={styles.logo}/>
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: 'white'
    },
    logo: {
        width: '100%',
        height: '100%',
        resizeMode: 'contain'
    }
})

export default Splash;
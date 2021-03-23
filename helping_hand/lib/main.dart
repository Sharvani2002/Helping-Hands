import 'package:flutter/material.dart';
import 'package:helping_hand/screens/welcome_screen.dart';
import 'package:helping_hand/screens/login_screen.dart';
import 'package:helping_hand/screens/registration_screen.dart';
import 'package:helping_hand/screens/profile_screen.dart';
import 'package:helping_hand/screens/home_screen.dart';
import 'package:helping_hand/screens/leaderboard_screen.dart';

void main() => runApp(HelpingHand());

class HelpingHand extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      initialRoute: ProfileScreen.id,
      routes: {
        WelcomeScreen.id: (context) => WelcomeScreen(),
        LoginScreen.id: (context) => LoginScreen(),
        RegistrationScreen.id: (context) => RegistrationScreen(),
        ProfileScreen.id: (context) => ProfileScreen(),
        HomeScreen.id: (context) => HomeScreen(),
        LeaderboardScreen.id: (context) => LeaderboardScreen(),
      },
    );
  }
}

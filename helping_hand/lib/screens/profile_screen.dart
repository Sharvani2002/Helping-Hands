import 'package:flutter/material.dart';
import 'package:helping_hand/components/rounded_button.dart';
import 'package:helping_hand/screens/home_screen.dart';

class ProfileScreen extends StatefulWidget {
  static String id = 'profile_screen';
  @override
  _ProfileScreenState createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
  @override
  Widget build(BuildContext context) {
    int _points = 0; // TODO set this up
    String _badge = 'nature-lover'; //TODO make this string later
    String _history = ''; // TODO set this up
    return Scaffold(
      appBar: AppBar(
        title: Text('Hello, xyz!'), //TODO add username functionality
      ),
      body: Padding(
          padding: EdgeInsets.symmetric(horizontal: 24.0),
          child: Column(
            children: <Widget>[
              Row(
                crossAxisAlignment: CrossAxisAlignment.end,
                children: [
                  RoundedButton(
                    title: 'Back',
                    color: Colors.blueGrey,
                    onPressed: () {
                      Navigator.pushNamed(context, HomeScreen.id);
                    },
                  )
                ],
              ),
              Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Container(
                    child: Text('Points: $_points'),
                  ),
                  SizedBox(
                    height: 8.0,
                  ),
                  Container(
                    child: Text('Badges: $_badge'),
                  ),
                  SizedBox(
                    height: 8.0,
                  ),
                  Container(
                    child: Text('History: $_history'),
                  ),
                  SizedBox(
                    height: 8.0,
                  ),
                  RoundedButton(
                    title: 'Claim Rewards',
                    color: Colors.lightBlueAccent,
                    onPressed: () {},
                  )
                ],
              )
            ],
          )),
    );
  }
}

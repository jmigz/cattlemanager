import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:mcattlemanager/screens/CattleListScreen.dart';

class SuccessPage extends StatelessWidget {
  Future<void> logout(BuildContext context) async {
    final prefs = await SharedPreferences.getInstance();
    prefs.setBool('isLoggedIn', false);
    Navigator.pushReplacementNamed(context, '/');
  }

  void navigateToCattleList(BuildContext context) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => CattleListScreen(),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Success'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              'You have successfully logged in!',
              style: TextStyle(fontSize: 24.0),
            ),
            SizedBox(height: 16.0),
            ElevatedButton(
              onPressed: () => navigateToCattleList(context),
              child: Text('Cattle List'),
            ),
            SizedBox(height: 16.0),
            ElevatedButton(
              onPressed: () => logout(context),
              child: Text('Logout'),
            ),
          ],
        ),
      ),
    );
  }
}

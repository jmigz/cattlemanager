import 'package:flutter/material.dart';
import 'package:postgres/postgres.dart';
import 'package:mcattlemanager/services/db_connection.dart';
import 'package:mcattlemanager/screens/SuccessPage.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({Key? key}) : super(key: key);

  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final TextEditingController _usernameController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
  final connection = dbConnection;

  @override
  void initState() {
    super.initState();
    _connectToDatabase();
  }

  void _connectToDatabase() async {
    try {
      await connection.open();
      print('Connected to the database');
    } catch (e) {
      print('Failed to connect to the database: $e');
    }
  }

  void _login(BuildContext context) async {
    final username = _usernameController.text;
    final password = _passwordController.text;

    try {
      final results = await connection.query(
        'SELECT * FROM users WHERE username = @username AND password = @password',
        substitutionValues: {'username': username, 'password': password},
      );

      if (results.isNotEmpty) {
        // Login successful
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => SuccessPage(),
          ),
        );
      } else {
        // Invalid username or password
        showDialog(
          context: context,
          builder: (context) => Builder(
            builder: (BuildContext context) {
              return AlertDialog(
                title: Text('Error'),
                content: Text('Invalid username or password.'),
                actions: [
                  TextButton(
                    onPressed: () => Navigator.pop(context),
                    child: Text('OK'),
                  ),
                ],
              );
            },
          ),
        );
      }
    } catch (e) {
      print('Failed to execute query: $e');
    }
  }

  @override
  void dispose() {
    connection.close();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Login'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            TextField(
              controller: _usernameController,
              decoration: const InputDecoration(
                labelText: 'Username',
              ),
            ),
            const SizedBox(height: 16),
            TextField(
              controller: _passwordController,
              obscureText: true,
              decoration: const InputDecoration(
                labelText: 'Password',
              ),
            ),
            const SizedBox(height: 24),
            ElevatedButton(
              onPressed: () => _login(context),
              child: const Text('Login'),
            ),
          ],
        ),
      ),
    );
  }
}

import 'package:flutter/material.dart';
import 'package:mcattlemanager/services/db_connection.dart';
import 'package:mcattlemanager/models/cattle.dart';

class AddCattleScreen extends StatelessWidget {
  final TextEditingController _breedController = TextEditingController();
  final TextEditingController _birthDateController = TextEditingController();
  final TextEditingController _sexController = TextEditingController();
  final TextEditingController _isPregnantController = TextEditingController();

  void _addCattle(BuildContext context) async {
    final String breed = _breedController.text;
    final DateTime birthDate = DateTime.parse(_birthDateController.text);
    final String sex = _sexController.text;
    final bool isPregnant = _isPregnantController.text.toLowerCase() == 'true';

    try {
      final cattle = Cattle(
        id: 0, // The database will auto-generate the ID
        breed: breed,
        birthDate: birthDate,
        age: calculateAge(birthDate), // Calculate age from birthDate
        weight: 0.0, // Set default weight to 0.0
        sex: sex,
        healthStatus: 'Healthy', // Set default health status
        isPregnant: isPregnant,
        vaccinations: 'None', // Set default vaccinations
        breedingHistory: 'None', // Set default breeding history
        isRemoved: false, // Set default isRemoved to false
        removalReason: '', // Set default removal reason to empty string
      );

      // Add the cattle to the database
      await dbConnection.transaction((connection) async {
        await connection.query(
          'INSERT INTO cattle (tag_number, breed, birth_date, age, weight, sex, health_status, is_pregnant, vaccinations, breeding_history, is_removed, removal_reason) '
              'VALUES (@tagNumber, @breed, @birthDate, @age, @weight, @sex, @healthStatus, @isPregnant, @vaccinations, @breedingHistory, @isRemoved, @removalReason)',
          substitutionValues: {
            'tagNumber': cattle.generateTagNumber(),
            'breed': cattle.breed,
            'birthDate': cattle.birthDate.toIso8601String(),
            'age': cattle.age,
            'weight': cattle.weight,
            'sex': cattle.sex,
            'healthStatus': cattle.healthStatus,
            'isPregnant': cattle.isPregnant,
            'vaccinations': cattle.vaccinations,
            'breedingHistory': cattle.breedingHistory,
            'isRemoved': cattle.isRemoved,
            'removalReason': cattle.removalReason,
          },
        );
      });

      showDialog(
        context: context,
        builder: (context) => AlertDialog(
          title: Text('Success'),
          content: Text('Cattle added successfully!'),
          actions: [
            TextButton(
              onPressed: () => Navigator.pop(context),
              child: Text('OK'),
            ),
          ],
        ),
      );

      // Clear the text fields after successful addition
      _breedController.clear();
      _birthDateController.clear();
      _sexController.clear();
      _isPregnantController.clear();
    } catch (e) {
      showDialog(
        context: context,
        builder: (context) => AlertDialog(
          title: Text('Error'),
          content: Text('Failed to add cattle: $e'),
          actions: [
            TextButton(
              onPressed: () => Navigator.pop(context),
              child: Text('OK'),
            ),
          ],
        ),
      );
    }
  }

  // Helper function to calculate age based on birthDate
  int calculateAge(DateTime birthDate) {
    final currentYear = DateTime.now().year;
    final birthYear = birthDate.year;
    return currentYear - birthYear + 1;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Add Cattle'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            TextField(
              controller: _breedController,
              decoration: InputDecoration(labelText: 'Breed'),
            ),
            TextField(
              controller: _birthDateController,
              decoration: InputDecoration(labelText: 'Birth Date (YYYY-MM-DD)'),
            ),
            TextField(
              controller: _sexController,
              decoration: InputDecoration(labelText: 'Sex'),
            ),
            TextField(
              controller: _isPregnantController,
              decoration: InputDecoration(labelText: 'Is Pregnant (true/false)'),
            ),
            ElevatedButton(
              onPressed: () => _addCattle(context),
              child: Text('Add Cattle'),
            ),
          ],
        ),
      ),
    );
  }
}

import 'package:flutter/material.dart';
import 'package:mcattlemanager/services/db_connection.dart';
import 'package:postgres/postgres.dart';
import 'package:mcattlemanager/models/cattle.dart';

class CattleListScreen extends StatefulWidget {
  @override
  _CattleListScreenState createState() => _CattleListScreenState();
}

class _CattleListScreenState extends State<CattleListScreen> {
  List<Cattle> cattleList = [];
  bool isLoading = true;

  @override
  void initState() {
    super.initState();
    fetchCattleList();
  }

  Future<void> fetchCattleList() async {
    try {
      final connection = dbConnection;

      await connection.open();
      final results = await connection.query('SELECT * FROM cattle');
      await connection.close();

      setState(() {
        cattleList = results
            .map((row) => Cattle(
          id: row[0] as int,
          tagNumber: row[1] as String,
          breed: row[2] as String,
          birthDate: row[3] as DateTime,
          age: row[4] as int,
          weight: row[5] as double,
          sex: row[6] as String,
          healthStatus: row[7] as String,
          isPregnant: row[8] as bool,
          vaccinations: row[9] as String,
          breedingHistory: row[10] as String,
          isRemoved: row[11] as bool,
          removalReason: row[12] as String,
        ))
            .toList();
        isLoading = false;
      });
    } catch (e) {
      setState(() {
        isLoading = false;
      });
      print('Error fetching cattle list: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Cattle List'),
      ),
      body: isLoading
          ? const Center(
        child: CircularProgressIndicator(),
      )
          : ListView.builder(
        itemCount: cattleList.length,
        itemBuilder: (context, index) {
          final cattle = cattleList[index];
          return ListTile(
            title: Text(cattle.tagNumber),
            subtitle: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text('Breed: ${cattle.breed}'),
                Text('Born: ${cattle.birthDate}'),
                Text('Sex: ${cattle.sex}'),
                Text('Removed: ${cattle.isRemoved}'),
                Text('Reason: ${cattle.removalReason}'),
              ],
            ),
            trailing: Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                IconButton(
                  icon: const Icon(Icons.edit),
                  onPressed: () {
                    // Implement edit functionality
                  },
                ),
                IconButton(
                  icon: const Icon(Icons.delete),
                  onPressed: () {
                    // Implement delete functionality
                  },
                ),
              ],
            ),
          );
        },
      ),
    );
  }
}
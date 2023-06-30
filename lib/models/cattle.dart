import 'package:meta/meta.dart';

class Cattle {
  final int id;
  final String tagNumber;
  final String breed;
  final DateTime birthDate;
  final int age;
  final double weight;
  final String sex;
  final String healthStatus;
  final bool isPregnant;
  final String vaccinations;
  final String breedingHistory;
  final bool isRemoved;
  final String removalReason;

  Cattle({
    required this.id,
    required this.tagNumber,
    required this.breed,
    required this.birthDate,
    required this.age,
    required this.weight,
    required this.sex,
    required this.healthStatus,
    required this.isPregnant,
    required this.vaccinations,
    required this.breedingHistory,
    required this.isRemoved,
    required this.removalReason,
  });

  // Helper method to calculate age based on birthDate
  int calculateAge(DateTime birthDate) {
    final currentYear = DateTime.now().year;
    final birthYear = birthDate.year;
    return currentYear - birthYear + 1;
  }

  // Helper method to generate the tag number based on the cattle's birth date
  String generateTagNumber() {
    final year = birthDate.year;
    final month = birthDate.month;

    // Replace this with the actual logic to get the latest cattle with a similar tag number from the database
    // You can query the database to get the latest cattle and extract the number from the tagNumber
    // For now, let's assume there are no cattle in the database with similar tag numbers
    // You may need to adjust this logic based on the actual implementation with the database.
    final latestNumber = 0;

    final newNumber = latestNumber + 1;

    return 'HF-${year.toString().substring(2)}-$month-$newNumber';
  }
}

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
}

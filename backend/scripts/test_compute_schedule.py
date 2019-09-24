import user

Sopin = user.User("TAM")
Sopin.load_subject_from_json("DEF101")
Sopin.load_subject_from_json("DEF102")
Sopin.load_subject_from_json("DEF103")
Sopin.load_subject_from_json("DEF104")
Sopin.load_subject_from_json("DEF105")

Sopin.compute_possible_schedules()


# imprimir los posibles resultados
for num_tope in Sopin.schedule_options:
    print("Horarios con " + str(num_tope) + " tope(s):")
    for schedule in Sopin.schedule_options[num_tope]:
        print(schedule.data)
    print("\n")
import Toybox.Lang;

// ---------------------------------------------------------------------------
// Rutinas de ejemplo incluidas en la app (MVP).
// En Fase 3 estas se reemplazan por rutinas definidas desde el móvil
// (App Settings -> JSON compacto que se parsea aquí).
// ---------------------------------------------------------------------------
module SampleData {

    // Devuelve la lista de sesiones disponibles.
    function sessions() as Array<Session> {
        return [
            fullBody(),
            pushDay()
        ];
    }

    function fullBody() as Session {
        return new Session("Full Body A", [
            new Exercise("Sentadilla", [
                new ExerciseSet(10, 40),
                new ExerciseSet(10, 40),
                new ExerciseSet(8, 45)
            ], 90),
            new Exercise("Press banca", [
                new ExerciseSet(10, 30),
                new ExerciseSet(10, 30),
                new ExerciseSet(8, 35)
            ], 90),
            new Exercise("Remo con barra", [
                new ExerciseSet(12, 30),
                new ExerciseSet(12, 30)
            ], 75)
        ]);
    }

    function pushDay() as Session {
        return new Session("Empuje", [
            new Exercise("Press militar", [
                new ExerciseSet(10, 25),
                new ExerciseSet(8, 27)
            ], 90),
            new Exercise("Fondos", [
                new ExerciseSet(12, 0),
                new ExerciseSet(10, 0)
            ], 60)
        ]);
    }
}

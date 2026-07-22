import Toybox.Lang;

// ---------------------------------------------------------------------------
// Modelo de datos
//   Session -> [Exercise] -> [ExerciseSet]
// Compacto a propósito: los relojes objetivo (Venu / Venu Sq) tienen poca RAM.
// ---------------------------------------------------------------------------

// Una serie individual: reps + carga.
class ExerciseSet {
    public var reps as Number;
    public var load as Number;      // en la unidad configurada (kg/lb)
    public var done as Boolean;

    public function initialize(reps as Number, load as Number) {
        self.reps = reps;
        self.load = load;
        self.done = false;
    }
}

// Un ejercicio: nombre + series + descanso entre series.
class Exercise {
    public var name as String;
    public var sets as Array<ExerciseSet>;
    public var restSeconds as Number;

    public function initialize(name as String, sets as Array<ExerciseSet>, restSeconds as Number) {
        self.name = name;
        self.sets = sets;
        self.restSeconds = restSeconds;
    }
}

// Una sesión completa de entrenamiento.
class Session {
    public var name as String;
    public var exercises as Array<Exercise>;

    public function initialize(name as String, exercises as Array<Exercise>) {
        self.name = name;
        self.exercises = exercises;
    }

    // Total de series de la sesión (para barra de progreso).
    public function totalSets() as Number {
        var total = 0;
        for (var i = 0; i < exercises.size(); i++) {
            total += exercises[i].sets.size();
        }
        return total;
    }

    // Subtítulo para el menú: "3 ejercicios · 8 series".
    public function subtitle() as String {
        return exercises.size() + " ejercicios · " + totalSets() + " series";
    }
}

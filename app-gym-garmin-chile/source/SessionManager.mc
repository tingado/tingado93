import Toybox.Lang;

// ---------------------------------------------------------------------------
// Lleva el estado de la sesión en curso: qué ejercicio y qué serie van,
// cuántas series se completaron y si la sesión terminó.
// ---------------------------------------------------------------------------
class SessionManager {
    public var session as Session;
    private var _exerciseIndex as Number;
    private var _setIndex as Number;
    private var _completedSets as Number;

    public function initialize(session as Session) {
        self.session = session;
        _exerciseIndex = 0;
        _setIndex = 0;
        _completedSets = 0;
    }

    public function currentExercise() as Exercise {
        return session.exercises[_exerciseIndex];
    }

    public function currentSet() as ExerciseSet {
        return currentExercise().sets[_setIndex];
    }

    // Número de serie (1-based) dentro del ejercicio actual.
    public function currentSetNumber() as Number {
        return _setIndex + 1;
    }

    public function totalSetsInExercise() as Number {
        return currentExercise().sets.size();
    }

    public function completedSets() as Number {
        return _completedSets;
    }

    public function totalSets() as Number {
        return session.totalSets();
    }

    // Descanso a aplicar tras completar la serie actual.
    public function currentRestSeconds() as Number {
        return currentExercise().restSeconds;
    }

    // Ajusta la carga de la serie actual (ej. ±2.5 kg), sin bajar de 0.
    public function adjustCurrentLoad(delta as Float) as Void {
        var set = currentSet();
        var newLoad = set.load + delta;
        set.load = (newLoad < 0.0) ? 0.0 : newLoad;
    }

    // Marca la serie actual como hecha y avanza el puntero.
    // Devuelve true si la sesión quedó COMPLETA.
    public function completeCurrentSet() as Boolean {
        currentSet().done = true;
        _completedSets++;

        if (_setIndex < currentExercise().sets.size() - 1) {
            _setIndex++;
            return false;
        }
        // Fin del ejercicio -> siguiente ejercicio.
        if (_exerciseIndex < session.exercises.size() - 1) {
            _exerciseIndex++;
            _setIndex = 0;
            return false;
        }
        // No hay más -> sesión completa.
        return true;
    }

    // ¿La serie que acabamos de completar era la última de todo? (sin descanso)
    public function isLastSetOverall() as Boolean {
        return _exerciseIndex == session.exercises.size() - 1
            && _setIndex == currentExercise().sets.size() - 1;
    }
}

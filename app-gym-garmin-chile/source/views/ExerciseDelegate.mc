using Toybox.WatchUi;
import Toybox.Lang;

// Interacción de la pantalla de ejercicio: confirmar "serie hecha".
// Tanto el toque en pantalla como el botón START disparan la misma acción.
class ExerciseDelegate extends WatchUi.BehaviorDelegate {
    private var _m as SessionManager;

    public function initialize(manager as SessionManager) {
        BehaviorDelegate.initialize();
        _m = manager;
    }

    private function markSetDone() as Boolean {
        // Capturamos el descanso del ejercicio actual ANTES de avanzar.
        var restSecs = _m.currentRestSeconds();
        var complete = _m.completeCurrentSet();

        if (complete) {
            Feedback.sessionComplete();
            WatchUi.switchToView(
                new CompleteView(_m),
                new CompleteDelegate(),
                WatchUi.SLIDE_UP
            );
        } else {
            Feedback.setDone();
            WatchUi.pushView(
                new RestView(_m, restSecs),
                new RestDelegate(),
                WatchUi.SLIDE_LEFT
            );
        }
        return true;
    }

    // Botón START / ENTER.
    public function onSelect() as Boolean {
        return markSetDone();
    }

    // Toque en pantalla táctil.
    public function onTap(evt as WatchUi.ClickEvent) as Boolean {
        return markSetDone();
    }

    // Deslizar arriba/abajo ajusta la carga de la serie actual (±2.5).
    public function onSwipe(evt as WatchUi.SwipeEvent) as Boolean {
        var dir = evt.getDirection();
        if (dir == WatchUi.SWIPE_UP) {
            _m.adjustCurrentLoad(2.5);
            WatchUi.requestUpdate();
            return true;
        } else if (dir == WatchUi.SWIPE_DOWN) {
            _m.adjustCurrentLoad(-2.5);
            WatchUi.requestUpdate();
            return true;
        }
        return false;
    }
}

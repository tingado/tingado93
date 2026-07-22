using Toybox.WatchUi;
import Toybox.Lang;

// Al terminar, cualquier acción vuelve al menú de sesiones.
class CompleteDelegate extends WatchUi.BehaviorDelegate {

    public function initialize() {
        BehaviorDelegate.initialize();
    }

    private function backToMenu() as Boolean {
        WatchUi.popView(WatchUi.SLIDE_DOWN);
        return true;
    }

    public function onSelect() as Boolean {
        return backToMenu();
    }

    public function onTap(evt as WatchUi.ClickEvent) as Boolean {
        return backToMenu();
    }

    public function onBack() as Boolean {
        return backToMenu();
    }
}

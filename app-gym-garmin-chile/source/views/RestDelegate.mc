using Toybox.WatchUi;
import Toybox.Lang;

// Permite saltar el descanso (toque o botón). El timer se detiene solo
// en RestView.onHide al desmontarse la vista.
class RestDelegate extends WatchUi.BehaviorDelegate {

    public function initialize() {
        BehaviorDelegate.initialize();
    }

    private function skip() as Boolean {
        WatchUi.popView(WatchUi.SLIDE_RIGHT);
        return true;
    }

    public function onSelect() as Boolean {
        return skip();
    }

    public function onTap(evt as WatchUi.ClickEvent) as Boolean {
        return skip();
    }

    public function onBack() as Boolean {
        return skip();
    }
}

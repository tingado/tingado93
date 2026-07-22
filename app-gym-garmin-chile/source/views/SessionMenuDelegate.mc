using Toybox.WatchUi;
import Toybox.Lang;

// Maneja la selección de sesión en el menú inicial.
class SessionMenuDelegate extends WatchUi.Menu2InputDelegate {
    private var _sessions as Array<Session>;

    public function initialize(sessions as Array<Session>) {
        Menu2InputDelegate.initialize();
        _sessions = sessions;
    }

    public function onSelect(item as WatchUi.MenuItem) as Void {
        var index = item.getId() as Number;
        var manager = new SessionManager(_sessions[index]);
        WatchUi.pushView(
            new ExerciseView(manager),
            new ExerciseDelegate(manager),
            WatchUi.SLIDE_LEFT
        );
    }
}

using Toybox.WatchUi;
using Toybox.Graphics;
using Toybox.Application;
import Toybox.Lang;

// Pantalla del ejercicio en curso: nombre, serie actual, reps x carga,
// y una barra de progreso de la sesión. Diseño centrado -> se adapta solo
// a pantalla redonda (Venu) y rectangular (Venu Sq).
class ExerciseView extends WatchUi.View {
    private var _m as SessionManager;

    public function initialize(manager as SessionManager) {
        View.initialize();
        _m = manager;
    }

    private function units() as String {
        var u = Application.Properties.getValue("units");
        return (u == null) ? "kg" : u;
    }

    public function onUpdate(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var h = dc.getHeight();
        var cx = w / 2;

        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_BLACK);
        dc.clear();

        var ex = _m.currentExercise();
        var set = _m.currentSet();

        // Nombre del ejercicio.
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(cx, h * 0.16, Graphics.FONT_SMALL, ex.name, Graphics.TEXT_JUSTIFY_CENTER);

        // "Serie 2 de 3".
        dc.setColor(Graphics.COLOR_LT_GRAY, Graphics.COLOR_TRANSPARENT);
        var serie = "Serie " + _m.currentSetNumber() + " de " + _m.totalSetsInExercise();
        dc.drawText(cx, h * 0.30, Graphics.FONT_TINY, serie, Graphics.TEXT_JUSTIFY_CENTER);

        // Dato principal: reps x carga (grande).
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        var main = (set.load > 0)
            ? set.reps + " x " + set.load + " " + units()
            : set.reps + " reps";
        dc.drawText(cx, h * 0.46, Graphics.FONT_NUMBER_MEDIUM, main, Graphics.TEXT_JUSTIFY_CENTER);

        // Barra de progreso de la sesión.
        var done = _m.completedSets();
        var total = _m.totalSets();
        var barW = (w * 0.6).toNumber();
        var barX = cx - barW / 2;
        var barY = (h * 0.74).toNumber();
        dc.setColor(Graphics.COLOR_DK_GRAY, Graphics.COLOR_TRANSPARENT);
        dc.fillRectangle(barX, barY, barW, 6);
        dc.setColor(Graphics.COLOR_GREEN, Graphics.COLOR_TRANSPARENT);
        dc.fillRectangle(barX, barY, (barW * done / total).toNumber(), 6);

        // Hint de acción.
        dc.setColor(Graphics.COLOR_LT_GRAY, Graphics.COLOR_TRANSPARENT);
        dc.drawText(cx, h * 0.84, Graphics.FONT_TINY,
            done + "/" + total + " · toca: serie hecha", Graphics.TEXT_JUSTIFY_CENTER);
    }
}

using Toybox.WatchUi;
using Toybox.Graphics;
import Toybox.Lang;

// Pantalla final: "SESIÓN COMPLETA" bien grande y en verde.
class CompleteView extends WatchUi.View {
    private var _m as SessionManager;

    public function initialize(manager as SessionManager) {
        View.initialize();
        _m = manager;
    }

    public function onUpdate(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var h = dc.getHeight();
        var cx = w / 2;

        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_BLACK);
        dc.clear();

        dc.setColor(Graphics.COLOR_GREEN, Graphics.COLOR_TRANSPARENT);
        dc.drawText(cx, h * 0.28, Graphics.FONT_MEDIUM, "SESIÓN", Graphics.TEXT_JUSTIFY_CENTER);
        dc.drawText(cx, h * 0.44, Graphics.FONT_MEDIUM, "COMPLETA", Graphics.TEXT_JUSTIFY_CENTER);

        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(cx, h * 0.66, Graphics.FONT_SMALL,
            _m.completedSets() + " series", Graphics.TEXT_JUSTIFY_CENTER);

        dc.setColor(Graphics.COLOR_LT_GRAY, Graphics.COLOR_TRANSPARENT);
        dc.drawText(cx, h * 0.84, Graphics.FONT_TINY, _m.session.name, Graphics.TEXT_JUSTIFY_CENTER);
    }
}

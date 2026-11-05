// stone:job stone:math.manhattan_safe
// stone:function manhattan_safe_rs

#[no_mangle]
pub extern "C" fn manhattan_safe_rs(x1: f64, y1: f64, x2: f64, y2: f64) -> f64 {
    if !(x1.is_finite() && y1.is_finite() && x2.is_finite() && y2.is_finite()) { return f64::NAN; }
    (x2 - x1).abs() + (y2 - y1).abs()
}

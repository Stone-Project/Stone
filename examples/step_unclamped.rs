// stone:job stone:math.step_unclamped
// stone:function step_unclamped_rs

#[no_mangle]
pub extern "C" fn step_unclamped_rs(edge: f64, x: f64, width: f64) -> f64 {
    if width <= 0.0 { return f64::NAN; }
    (x - edge) / width + 0.5
}

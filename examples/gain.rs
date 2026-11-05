// stone:job stone:math.gain
// stone:function gain_rs

#[no_mangle]
pub extern "C" fn gain_rs(x: f64) -> f64 {
    if x < 0.5 { 0.5 * (2.0 * x).sqrt() } else { 1.0 - 0.5 * (2.0 * (1.0 - x)).sqrt() }
}

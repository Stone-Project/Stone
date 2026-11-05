// stone:job stone:math.clamp01
// stone:function clamp01_rs

#[no_mangle]
pub extern "C" fn clamp01_rs(x: f64) -> f64 {
    if x < 0.0 { 0.0 } else if x > 1.0 { 1.0 } else { x }
}

// stone:job stone:math.lerp_unclamped
// stone:function lerp_unclamped_rs

#[no_mangle]
pub extern "C" fn lerp_unclamped_rs(a: f64, b: f64, t: f64) -> f64 { a + (b - a) * t }

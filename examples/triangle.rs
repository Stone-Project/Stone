// stone:job stone:math.triangle
// stone:function triangle_rs

#[no_mangle]
pub extern "C" fn triangle_rs(x: f64) -> f64 { (x.rem_euclid(2.0) - 1.0).abs() }

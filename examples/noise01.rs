// stone:job stone:math.noise01
// stone:function noise01_rs

#[no_mangle]
pub extern "C" fn noise01_rs(x: f64) -> f64 { (x * 12.9898).rem_euclid(1.0).abs() }

// stone:job stone:math.hash01
// stone:function hash01_rs

#[no_mangle]
pub extern "C" fn hash01_rs(x: f64) -> f64 { (x * 0.1031).rem_euclid(1.0).abs() }

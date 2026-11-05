// stone:job stone:math.pingpong
// stone:function pingpong_rs

#[no_mangle]
pub extern "C" fn pingpong_rs(x: f64, length: f64) -> f64 { (x.rem_euclid(2.0 * length) - length).abs() }

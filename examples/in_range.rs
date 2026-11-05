// stone:job stone:math.in_range
// stone:function in_range_rs

#[no_mangle]
pub extern "C" fn in_range_rs(x: f64, low: f64, high: f64) -> bool { low <= x && x <= high }

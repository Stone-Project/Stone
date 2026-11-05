// stone:job stone:math.snap
// stone:function snap_rs

#[no_mangle]
pub extern "C" fn snap_rs(x: f64, step: f64) -> f64 { ((x + step / 2.0) / step).floor() * step }
